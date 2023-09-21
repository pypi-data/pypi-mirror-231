import scipy.ndimage

from CDEng import *


def create_ht_matrix(seq):
    mat = np.zeros([len(seq), len(seq)])
    for i in range(len(seq)):
        mat[i, :] = np.roll(seq, i)
    return mat


def expandSequence(seq, osFactor=200, singlePulse=False, scaleFactor=0.5):
    '''
    Expand a PRBS by a target over sampling factor (osFactor)
    scaleFactor can be used to scale the matrix if needed.
    '''

    seqLen = len(seq)
    newSeq = np.zeros(osFactor * len(seq))
    j = -1
    maxVal = seq.max() * scaleFactor
    minVal = seq.min() * scaleFactor
    for i, v in enumerate(newSeq):  # go through each element
        if i % osFactor == 0:  # reset count when the oversampling factor is reached
            j += 1  # start counting upward
            curVal = seq[j]

            if singlePulse:
                if curVal > maxVal:
                    newSeq[i] = curVal
                    curVal = 0
                elif curVal < minVal:

                    newSeq[i] = curVal
                    curVal = 0
                else:
                    curVal = 0

            else:
                newSeq[i] = curVal
        else:
            newSeq[i] = curVal

    return newSeq


class UniDecHT(UniDecCD):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("HT-CD-MS Engine")
        self.scans = []

        self.htseq = '1110100'  # '0000100101100111110001101110101'
        self.oversampling = 200  # Oversampling factor
        self.timespacing = 0.165576

    def process_data(self, transform=True):
        """
        Main function for processing CDMS data, includes filtering, converting intensity to charge, histogramming,
        processing the histograms, and transforming (if specified). Transforming is sometimes unnecessary, which is why
        it can be turned off for speed.

        :param transform: Sets whether to transform the data from m/z to mass. Default True.
        :return: None
        """
        starttime = time.perf_counter()
        # Copy filtered array and delete peaks.
        self.farray = deepcopy(self.darray)
        self.pks = peakstructure.Peaks()
        print("Filtering m/z range:", self.config.minmz, self.config.maxmz, "Start Length:", len(self.farray))
        self.filter_mz(mzrange=[self.config.minmz, self.config.maxmz])
        print("Filtering centroids:", self.config.CDres, "Start Length:", len(self.farray))
        self.filter_centroid_all(self.config.CDres)
        print("Filtering Charge range:", self.config.startz, self.config.endz, "Start Length:", len(self.farray))
        self.filter_z(zrange=[self.config.startz, self.config.endz + 1])

        print("Converting From Intensity to Charge. Slope:", self.config.CDslope, "Start Length:", len(self.farray))
        self.convert(slope=self.config.CDslope)

        self.scans = np.unique(self.farray[:, 2])
        self.fullscans = np.arange(1, np.amax(self.scans) + 1)

        self.topfarray = deepcopy(self.farray)
        self.topzarray = deepcopy(self.zarray)

        self.prep_hist(mzbins=self.config.mzbins, zbins=self.config.CDzbins)

        self.hstack = np.zeros((len(self.scans), self.topharray.shape[0], self.topharray.shape[1]))

        for i, s in enumerate(self.scans):
            b1 = self.topfarray[:, 2] == s
            self.farray = self.topfarray[b1]
            self.zarray = self.topzarray[b1]
            print(self.farray)
            print(self.zarray)

            print("Creating Histogram Bins:", self.config.mzbins, self.config.CDzbins, "Start Length:",
                  len(self.farray))
            print(self.config.mzbins, self.config.CDzbins)
            self.histogramLC()

            # NEED TO WORK ON THIS SECTION
            if len(self.harray) > 0 and np.amax(self.harray) > 0 and False:
                self.hist_data_prep()
                print("Transforming m/z to mass:", self.config.massbins, "Start Length:", len(self.farray))
                if transform:
                    self.transform()
                    self.unprocessed = deepcopy(self.data.massdat)
            else:
                print("ERROR: Empty histogram array on process")

            self.topharray += self.harray
            self.hstack[i] = self.harray

        if self.config.datanorm == 1:
            maxval = np.amax(self.topharray)
            if maxval > 0:
                self.topharray /= maxval

        self.data.data3 = np.transpose([np.ravel(self.X, order="F"), np.ravel(self.Y, order="F"),
                                        np.ravel(self.topharray, order="F")])
        print("Process Time:", time.perf_counter() - starttime)

    def prep_hist(self, mzbins=1, zbins=1, mzrange=None, zrange=None):
        # Set up parameters
        if mzbins < 0.001:
            print("Error, mzbins too small. Changing to 1", mzbins)
            mzbins = 1
            self.config.mzbins = 1
        self.config.mzbins = mzbins
        self.config.CDzbins = zbins

        x = self.farray[:, 0]
        y = self.zarray
        # Set Up Ranges
        if mzrange is None:
            mzrange = [np.floor(np.amin(x)), np.amax(x)]
        if zrange is None:
            zrange = [np.floor(np.amin(y)), np.amax(y)]

        # Create Axes
        mzaxis = np.arange(mzrange[0] - mzbins / 2., mzrange[1] + mzbins / 2, mzbins)
        # Weird fix to make this axis even is necessary for CuPy fft for some reason...
        if len(mzaxis) % 2 == 1:
            mzaxis = np.arange(mzrange[0] - mzbins / 2., mzrange[1] + 3 * mzbins / 2, mzbins)
        zaxis = np.arange(zrange[0] - zbins / 2., zrange[1] + zbins / 2, zbins)
        self.mzaxis = mzaxis
        self.zaxis = zaxis

        self.topharray, self.mz, self.ztab = np.histogram2d([], [], [self.mzaxis, self.zaxis])
        self.topharray = np.transpose(self.topharray)

        self.mz = self.mz[1:] - self.config.mzbins / 2.
        self.ztab = self.ztab[1:] - self.config.CDzbins / 2.
        self.data.ztab = self.ztab
        self.X, self.Y = np.meshgrid(self.mz, self.ztab, indexing='xy')
        self.mass = (self.X - self.config.adductmass) * self.Y

    def histogramLC(self, x=None, y=None):
        if x is None:
            x = self.farray[:, 0]

        if y is None:
            y = self.zarray

        if len(x) == 0 or len(y) == 0:
            print("ERROR: Empty Filtered Array, check settings")
            self.harray = np.zeros_like(self.topharray)
            return self.harray

        self.harray, mz, ztab = np.histogram2d(x, y, [self.mzaxis, self.zaxis])
        self.harray = np.transpose(self.harray)

        return self.harray

    def tic_ht(self):
        self.tic = np.sum(self.hstack, axis=(1, 2))
        self.tic /= np.amax(self.tic)

        self.fulltic = np.zeros_like(self.fullscans)
        for i, s in enumerate(self.scans):
            self.fulltic[int(s) - 1] = self.tic[i]
        self.fulltic = scipy.ndimage.gaussian_filter1d(self.fulltic, 4)
        self.setup_ht()
        fftk = np.fft.fft(self.htkernel).conj()
        self.htoutput = np.fft.ifft(np.fft.fft(self.fulltic) * fftk).real

    def setup_ht(self):
        # Convert sequence to array
        seqarray = np.array([int(s) for s in self.htseq])
        htmatrix = create_ht_matrix(seqarray)
        invhtmat = np.linalg.inv(htmatrix)
        shortkernel = invhtmat[:, 0]
        scaledkernel = np.arange(len(shortkernel)) / (len(shortkernel))
        kernelscans = scaledkernel * np.amax(self.scans)

        self.htkernel = np.zeros_like(self.fullscans)
        index = 0
        for i, s in enumerate(self.fullscans):
            # check if this is the first scan above the next scaledkernel
            if s >= kernelscans[index]:
                self.htkernel[i] = shortkernel[index]
                index += 1
                if index >= len(shortkernel):
                    break

    def run_ht(self):
        # create full hstack
        self.fullhstack = np.zeros((len(self.fullscans), self.topharray.shape[0], self.topharray.shape[1]))
        self.fullhstack_ht = np.zeros((len(self.fullscans), self.topharray.shape[0], self.topharray.shape[1]))
        for i, s in enumerate(self.scans):
            self.fullhstack[int(s) - 1] = self.hstack[i]


        fftk = np.fft.fft(self.htkernel).conj()
        for i, x in enumerate(self.mz):
            for j, y in enumerate(self.ztab):
                trace = self.fullhstack[:, j, i]
                trace = scipy.ndimage.gaussian_filter1d(trace, 5)
                htoutput = np.fft.ifft(np.fft.fft(trace) * fftk).real
                self.fullhstack_ht[:, j, i] = htoutput




if __name__ == '__main__':

    eng = UniDecHT()

    dir = "C:\Data\HT-CD-MS"
    os.chdir(dir)
    path = "C:\\Data\\HT-CD-MS\\20230906 JDS BSA SEC f22 10x dilute STORI high flow 1_20230906171314_2023-09-07-01-43-26.dmt"

    eng.open_file(path)
    eng.process_data()
    eng.tic_ht()
    eng.run_ht()
    print(np.shape(eng.hstack))

    import matplotlib.pyplot as plt

    plt.plot(eng.fullscans, eng.fulltic)
    plt.plot(eng.fullscans, eng.htkernel)
    plt.plot(eng.fullscans, eng.htoutput)
    plt.show()

    plt.figure()

    plt.subplot(121)
    for i, x in enumerate(eng.mz):
        for j, y in enumerate(eng.ztab):
            plt.plot(eng.fullscans, eng.fullhstack_ht[:, j, i])

    plt.subplot(122)
    plt.imshow(np.sum(eng.fullhstack[:150], axis=0), aspect="auto", origin="lower",
               extent=[eng.mz[0], eng.mz[-1], eng.ztab[0], eng.ztab[-1]])

    plt.show()


    from unidec.modules import PlotAnimations as PA
    import wx

    app = wx.App(False)
    PA.AnimationWindow(None, eng.fullhstack[50:], mode="2D")
    app.MainLoop()
