
NUM_DIMS = None
HAS_CHANNEL_DIM = False
HAS_BATCH_DIM = False


def num_dims(_num_dims):
    # global NUM_DIMS
    # NUM_DIMS = _num_dims
    variables = globals()
    variables["NUM_DIMS"] = _num_dims


def has_channel_dim(_has_channel_dim):
    # global HAS_CHANNEL_DIM
    # HAS_CHANNEL_DIM = _has_channel_dim
    variables = globals()
    variables["HAS_CHANNEL_DIM"] = _has_channel_dim


def has_batch_dim(_has_batch_dim):
    # global HAS_BATCH_DIM
    # HAS_BATCH_DIM = _has_batch_dim
    variables = globals()
    variables["HAS_BATCH_DIM"] = _has_batch_dim
