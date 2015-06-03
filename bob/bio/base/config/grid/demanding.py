import bob.bio.base

# define a queue with demanding parameters
grid = bob.bio.base.grid.Grid(
  training_queue = '32G',
  # preprocessing
  preprocessing_queue = '4G',
  # feature extraction
  extraction_queue = '8G',
  # feature projection
  projection_queue = '8G',
  # model enrollment
  enrollment_queue = '8G',
  # scoring
  scoring_queue = '8G'
)
