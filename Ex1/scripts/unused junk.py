import math
import numpy as np

def pre_process(filename, frame_size=2048, frame_rate=FPS, num_bands=40, **kwargs):
    """
    Pre-process the audio signal.

    Parameters
    ----------
    filename : str
        File to be processed.
    frame_size : int
        Size of the frames.
    frame_rate : float
        Frame rate used for the STFT.
    num_bands : int
        Number of frequency bands for the Mel filterbank.
    kwargs : dict, optional
        Additional keyword arguments.

    Returns
    -------
    spectrogram : numpy array
        Spectrogram.

    """
    ######## COMPUTE FRAMES ########
    
    sr = 44100 # samping rate    
    hop_size = int(sr / frame_rate) # hop size depends on sampling rate and frame rate
    signal, sr = librosa.load(filename, sr=sr) # read file
    
    # number of frames without remainder frame
    full_frames = int(len(signal) / hop_size)
    
    # compute 0 padded signal
    front_padded_signal = np.concatenate((np.zeros(int(frame_size/2)), signal))
    end_zeros = full_frames * hop_size + frame_size - len(front_padded_signal)
    padded_signal = np.concatenate((front_padded_signal, np.zeros(end_zeros)))
    
    # compute frames
    frames = []
    for i in range(full_frames+1):
        index = i*hop_size
        frame = padded_signal[index : index+2048]
        frames.append(frame)
        
    
    # madmom to double check
    frames_madmom = madmom.audio.signal.FramedSignal(signal)
    
    """
    print("signal length:", len(signal))
    print("end zeros:", end_zeros)
    print("padded signal length:",len(padded_signal))
    
    print("")
    print(frames_madmom[10])
    print(frames[10])
    """
    
    ######## FFT ########

    fft = librosa.core.fft_frequencies(sr=sr, n_fft=int(frame_size/2))
    print(fft.shape)
    
    spectrogram = None
    return spectrogram