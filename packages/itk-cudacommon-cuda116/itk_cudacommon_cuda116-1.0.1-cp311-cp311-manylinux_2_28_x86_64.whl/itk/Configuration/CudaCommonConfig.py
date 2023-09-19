depends = ('ITKPyBase', 'ITKCommon', )
templates = (  ('CudaDataManager', 'itk::CudaDataManager', 'itkCudaDataManager', True),
  ('CudaImage', 'itk::CudaImage', 'itkCudaImageUC2', True, 'unsigned char, 2'),
  ('CudaImage', 'itk::CudaImage', 'itkCudaImageUL2', True, 'unsigned long, 2'),
  ('CudaImage', 'itk::CudaImage', 'itkCudaImageSS2', True, 'signed short, 2'),
  ('CudaImage', 'itk::CudaImage', 'itkCudaImageUS2', True, 'unsigned short, 2'),
  ('CudaImage', 'itk::CudaImage', 'itkCudaImageF2', True, 'float, 2'),
  ('CudaImage', 'itk::CudaImage', 'itkCudaImageD2', True, 'double, 2'),
  ('CudaImage', 'itk::CudaImage', 'itkCudaImageUC3', True, 'unsigned char, 3'),
  ('CudaImage', 'itk::CudaImage', 'itkCudaImageUL3', True, 'unsigned long, 3'),
  ('CudaImage', 'itk::CudaImage', 'itkCudaImageSS3', True, 'signed short, 3'),
  ('CudaImage', 'itk::CudaImage', 'itkCudaImageUS3', True, 'unsigned short, 3'),
  ('CudaImage', 'itk::CudaImage', 'itkCudaImageF3', True, 'float, 3'),
  ('CudaImage', 'itk::CudaImage', 'itkCudaImageD3', True, 'double, 3'),
  ('CudaImage', 'itk::CudaImage', 'itkCudaImageUC4', True, 'unsigned char, 4'),
  ('CudaImage', 'itk::CudaImage', 'itkCudaImageUL4', True, 'unsigned long, 4'),
  ('CudaImage', 'itk::CudaImage', 'itkCudaImageSS4', True, 'signed short, 4'),
  ('CudaImage', 'itk::CudaImage', 'itkCudaImageUS4', True, 'unsigned short, 4'),
  ('CudaImage', 'itk::CudaImage', 'itkCudaImageF4', True, 'float, 4'),
  ('CudaImage', 'itk::CudaImage', 'itkCudaImageD4', True, 'double, 4'),
  ('CudaImage', 'itk::CudaImage', 'itkCudaImageVF22', True, 'itk::Vector< float,2 >, 2'),
  ('CudaImage', 'itk::CudaImage', 'itkCudaImageCVF22', True, 'itk::CovariantVector< float,2 >, 2'),
  ('CudaImage', 'itk::CudaImage', 'itkCudaImageVF23', True, 'itk::Vector< float,2 >, 3'),
  ('CudaImage', 'itk::CudaImage', 'itkCudaImageCVF23', True, 'itk::CovariantVector< float,2 >, 3'),
  ('CudaImage', 'itk::CudaImage', 'itkCudaImageVF24', True, 'itk::Vector< float,2 >, 4'),
  ('CudaImage', 'itk::CudaImage', 'itkCudaImageCVF24', True, 'itk::CovariantVector< float,2 >, 4'),
  ('CudaImage', 'itk::CudaImage', 'itkCudaImageVF32', True, 'itk::Vector< float,3 >, 2'),
  ('CudaImage', 'itk::CudaImage', 'itkCudaImageCVF32', True, 'itk::CovariantVector< float,3 >, 2'),
  ('CudaImage', 'itk::CudaImage', 'itkCudaImageVF33', True, 'itk::Vector< float,3 >, 3'),
  ('CudaImage', 'itk::CudaImage', 'itkCudaImageCVF33', True, 'itk::CovariantVector< float,3 >, 3'),
  ('CudaImage', 'itk::CudaImage', 'itkCudaImageVF34', True, 'itk::Vector< float,3 >, 4'),
  ('CudaImage', 'itk::CudaImage', 'itkCudaImageCVF34', True, 'itk::CovariantVector< float,3 >, 4'),
  ('CudaImage', 'itk::CudaImage', 'itkCudaImageVF42', True, 'itk::Vector< float,4 >, 2'),
  ('CudaImage', 'itk::CudaImage', 'itkCudaImageCVF42', True, 'itk::CovariantVector< float,4 >, 2'),
  ('CudaImage', 'itk::CudaImage', 'itkCudaImageVF43', True, 'itk::Vector< float,4 >, 3'),
  ('CudaImage', 'itk::CudaImage', 'itkCudaImageCVF43', True, 'itk::CovariantVector< float,4 >, 3'),
  ('CudaImage', 'itk::CudaImage', 'itkCudaImageVF44', True, 'itk::Vector< float,4 >, 4'),
  ('CudaImage', 'itk::CudaImage', 'itkCudaImageCVF44', True, 'itk::CovariantVector< float,4 >, 4'),
  ('CudaImageDataManager', 'itk::CudaImageDataManager', 'itkCudaImageDataManagerCIUC2', True, 'itk::CudaImage<unsigned char, 2>'),
  ('CudaImageDataManager', 'itk::CudaImageDataManager', 'itkCudaImageDataManagerCIUL2', True, 'itk::CudaImage<unsigned long, 2>'),
  ('CudaImageDataManager', 'itk::CudaImageDataManager', 'itkCudaImageDataManagerCISS2', True, 'itk::CudaImage<signed short, 2>'),
  ('CudaImageDataManager', 'itk::CudaImageDataManager', 'itkCudaImageDataManagerCIUS2', True, 'itk::CudaImage<unsigned short, 2>'),
  ('CudaImageDataManager', 'itk::CudaImageDataManager', 'itkCudaImageDataManagerCIF2', True, 'itk::CudaImage<float, 2>'),
  ('CudaImageDataManager', 'itk::CudaImageDataManager', 'itkCudaImageDataManagerCID2', True, 'itk::CudaImage<double, 2>'),
  ('CudaImageDataManager', 'itk::CudaImageDataManager', 'itkCudaImageDataManagerCIUC3', True, 'itk::CudaImage<unsigned char, 3>'),
  ('CudaImageDataManager', 'itk::CudaImageDataManager', 'itkCudaImageDataManagerCIUL3', True, 'itk::CudaImage<unsigned long, 3>'),
  ('CudaImageDataManager', 'itk::CudaImageDataManager', 'itkCudaImageDataManagerCISS3', True, 'itk::CudaImage<signed short, 3>'),
  ('CudaImageDataManager', 'itk::CudaImageDataManager', 'itkCudaImageDataManagerCIUS3', True, 'itk::CudaImage<unsigned short, 3>'),
  ('CudaImageDataManager', 'itk::CudaImageDataManager', 'itkCudaImageDataManagerCIF3', True, 'itk::CudaImage<float, 3>'),
  ('CudaImageDataManager', 'itk::CudaImageDataManager', 'itkCudaImageDataManagerCID3', True, 'itk::CudaImage<double, 3>'),
  ('CudaImageDataManager', 'itk::CudaImageDataManager', 'itkCudaImageDataManagerCIUC4', True, 'itk::CudaImage<unsigned char, 4>'),
  ('CudaImageDataManager', 'itk::CudaImageDataManager', 'itkCudaImageDataManagerCIUL4', True, 'itk::CudaImage<unsigned long, 4>'),
  ('CudaImageDataManager', 'itk::CudaImageDataManager', 'itkCudaImageDataManagerCISS4', True, 'itk::CudaImage<signed short, 4>'),
  ('CudaImageDataManager', 'itk::CudaImageDataManager', 'itkCudaImageDataManagerCIUS4', True, 'itk::CudaImage<unsigned short, 4>'),
  ('CudaImageDataManager', 'itk::CudaImageDataManager', 'itkCudaImageDataManagerCIF4', True, 'itk::CudaImage<float, 4>'),
  ('CudaImageDataManager', 'itk::CudaImageDataManager', 'itkCudaImageDataManagerCID4', True, 'itk::CudaImage<double, 4>'),
  ('CudaImageDataManager', 'itk::CudaImageDataManager', 'itkCudaImageDataManagerCIVF22', True, 'itk::CudaImage<itk::Vector< float,2 >, 2>'),
  ('CudaImageDataManager', 'itk::CudaImageDataManager', 'itkCudaImageDataManagerCICVF22', True, 'itk::CudaImage<itk::CovariantVector< float,2 >, 2>'),
  ('CudaImageDataManager', 'itk::CudaImageDataManager', 'itkCudaImageDataManagerCIVF23', True, 'itk::CudaImage<itk::Vector< float,2 >, 3>'),
  ('CudaImageDataManager', 'itk::CudaImageDataManager', 'itkCudaImageDataManagerCICVF23', True, 'itk::CudaImage<itk::CovariantVector< float,2 >, 3>'),
  ('CudaImageDataManager', 'itk::CudaImageDataManager', 'itkCudaImageDataManagerCIVF24', True, 'itk::CudaImage<itk::Vector< float,2 >, 4>'),
  ('CudaImageDataManager', 'itk::CudaImageDataManager', 'itkCudaImageDataManagerCICVF24', True, 'itk::CudaImage<itk::CovariantVector< float,2 >, 4>'),
  ('CudaImageDataManager', 'itk::CudaImageDataManager', 'itkCudaImageDataManagerCIVF32', True, 'itk::CudaImage<itk::Vector< float,3 >, 2>'),
  ('CudaImageDataManager', 'itk::CudaImageDataManager', 'itkCudaImageDataManagerCICVF32', True, 'itk::CudaImage<itk::CovariantVector< float,3 >, 2>'),
  ('CudaImageDataManager', 'itk::CudaImageDataManager', 'itkCudaImageDataManagerCIVF33', True, 'itk::CudaImage<itk::Vector< float,3 >, 3>'),
  ('CudaImageDataManager', 'itk::CudaImageDataManager', 'itkCudaImageDataManagerCICVF33', True, 'itk::CudaImage<itk::CovariantVector< float,3 >, 3>'),
  ('CudaImageDataManager', 'itk::CudaImageDataManager', 'itkCudaImageDataManagerCIVF34', True, 'itk::CudaImage<itk::Vector< float,3 >, 4>'),
  ('CudaImageDataManager', 'itk::CudaImageDataManager', 'itkCudaImageDataManagerCICVF34', True, 'itk::CudaImage<itk::CovariantVector< float,3 >, 4>'),
  ('CudaImageDataManager', 'itk::CudaImageDataManager', 'itkCudaImageDataManagerCIVF42', True, 'itk::CudaImage<itk::Vector< float,4 >, 2>'),
  ('CudaImageDataManager', 'itk::CudaImageDataManager', 'itkCudaImageDataManagerCICVF42', True, 'itk::CudaImage<itk::CovariantVector< float,4 >, 2>'),
  ('CudaImageDataManager', 'itk::CudaImageDataManager', 'itkCudaImageDataManagerCIVF43', True, 'itk::CudaImage<itk::Vector< float,4 >, 3>'),
  ('CudaImageDataManager', 'itk::CudaImageDataManager', 'itkCudaImageDataManagerCICVF43', True, 'itk::CudaImage<itk::CovariantVector< float,4 >, 3>'),
  ('CudaImageDataManager', 'itk::CudaImageDataManager', 'itkCudaImageDataManagerCIVF44', True, 'itk::CudaImage<itk::Vector< float,4 >, 4>'),
  ('CudaImageDataManager', 'itk::CudaImageDataManager', 'itkCudaImageDataManagerCICVF44', True, 'itk::CudaImage<itk::CovariantVector< float,4 >, 4>'),
  ('ImageSource', 'itk::ImageSource', 'itkImageSourceCIUC2', False, 'itk::CudaImage<unsigned char, 2>'),
  ('ImageSource', 'itk::ImageSource', 'itkImageSourceCIUL2', False, 'itk::CudaImage<unsigned long, 2>'),
  ('ImageSource', 'itk::ImageSource', 'itkImageSourceCISS2', False, 'itk::CudaImage<signed short, 2>'),
  ('ImageSource', 'itk::ImageSource', 'itkImageSourceCIUS2', False, 'itk::CudaImage<unsigned short, 2>'),
  ('ImageSource', 'itk::ImageSource', 'itkImageSourceCIF2', False, 'itk::CudaImage<float, 2>'),
  ('ImageSource', 'itk::ImageSource', 'itkImageSourceCID2', False, 'itk::CudaImage<double, 2>'),
  ('ImageSource', 'itk::ImageSource', 'itkImageSourceCIUC3', False, 'itk::CudaImage<unsigned char, 3>'),
  ('ImageSource', 'itk::ImageSource', 'itkImageSourceCIUL3', False, 'itk::CudaImage<unsigned long, 3>'),
  ('ImageSource', 'itk::ImageSource', 'itkImageSourceCISS3', False, 'itk::CudaImage<signed short, 3>'),
  ('ImageSource', 'itk::ImageSource', 'itkImageSourceCIUS3', False, 'itk::CudaImage<unsigned short, 3>'),
  ('ImageSource', 'itk::ImageSource', 'itkImageSourceCIF3', False, 'itk::CudaImage<float, 3>'),
  ('ImageSource', 'itk::ImageSource', 'itkImageSourceCID3', False, 'itk::CudaImage<double, 3>'),
  ('ImageSource', 'itk::ImageSource', 'itkImageSourceCIUC4', False, 'itk::CudaImage<unsigned char, 4>'),
  ('ImageSource', 'itk::ImageSource', 'itkImageSourceCIUL4', False, 'itk::CudaImage<unsigned long, 4>'),
  ('ImageSource', 'itk::ImageSource', 'itkImageSourceCISS4', False, 'itk::CudaImage<signed short, 4>'),
  ('ImageSource', 'itk::ImageSource', 'itkImageSourceCIUS4', False, 'itk::CudaImage<unsigned short, 4>'),
  ('ImageSource', 'itk::ImageSource', 'itkImageSourceCIF4', False, 'itk::CudaImage<float, 4>'),
  ('ImageSource', 'itk::ImageSource', 'itkImageSourceCID4', False, 'itk::CudaImage<double, 4>'),
  ('ImageSource', 'itk::ImageSource', 'itkImageSourceCIVF22', False, 'itk::CudaImage<itk::Vector< float,2 >, 2>'),
  ('ImageSource', 'itk::ImageSource', 'itkImageSourceCICVF22', False, 'itk::CudaImage<itk::CovariantVector< float,2 >, 2>'),
  ('ImageSource', 'itk::ImageSource', 'itkImageSourceCIVF23', False, 'itk::CudaImage<itk::Vector< float,2 >, 3>'),
  ('ImageSource', 'itk::ImageSource', 'itkImageSourceCICVF23', False, 'itk::CudaImage<itk::CovariantVector< float,2 >, 3>'),
  ('ImageSource', 'itk::ImageSource', 'itkImageSourceCIVF24', False, 'itk::CudaImage<itk::Vector< float,2 >, 4>'),
  ('ImageSource', 'itk::ImageSource', 'itkImageSourceCICVF24', False, 'itk::CudaImage<itk::CovariantVector< float,2 >, 4>'),
  ('ImageSource', 'itk::ImageSource', 'itkImageSourceCIVF32', False, 'itk::CudaImage<itk::Vector< float,3 >, 2>'),
  ('ImageSource', 'itk::ImageSource', 'itkImageSourceCICVF32', False, 'itk::CudaImage<itk::CovariantVector< float,3 >, 2>'),
  ('ImageSource', 'itk::ImageSource', 'itkImageSourceCIVF33', False, 'itk::CudaImage<itk::Vector< float,3 >, 3>'),
  ('ImageSource', 'itk::ImageSource', 'itkImageSourceCICVF33', False, 'itk::CudaImage<itk::CovariantVector< float,3 >, 3>'),
  ('ImageSource', 'itk::ImageSource', 'itkImageSourceCIVF34', False, 'itk::CudaImage<itk::Vector< float,3 >, 4>'),
  ('ImageSource', 'itk::ImageSource', 'itkImageSourceCICVF34', False, 'itk::CudaImage<itk::CovariantVector< float,3 >, 4>'),
  ('ImageSource', 'itk::ImageSource', 'itkImageSourceCIVF42', False, 'itk::CudaImage<itk::Vector< float,4 >, 2>'),
  ('ImageSource', 'itk::ImageSource', 'itkImageSourceCICVF42', False, 'itk::CudaImage<itk::CovariantVector< float,4 >, 2>'),
  ('ImageSource', 'itk::ImageSource', 'itkImageSourceCIVF43', False, 'itk::CudaImage<itk::Vector< float,4 >, 3>'),
  ('ImageSource', 'itk::ImageSource', 'itkImageSourceCICVF43', False, 'itk::CudaImage<itk::CovariantVector< float,4 >, 3>'),
  ('ImageSource', 'itk::ImageSource', 'itkImageSourceCIVF44', False, 'itk::CudaImage<itk::Vector< float,4 >, 4>'),
  ('ImageSource', 'itk::ImageSource', 'itkImageSourceCICVF44', False, 'itk::CudaImage<itk::CovariantVector< float,4 >, 4>'),
)
factories = ()
