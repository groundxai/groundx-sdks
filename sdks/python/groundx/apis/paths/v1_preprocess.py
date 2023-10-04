from groundx.paths.v1_preprocess.get import ApiForget
from groundx.paths.v1_preprocess.post import ApiForpost
from groundx.paths.v1_preprocess.delete import ApiFordelete


class V1Preprocess(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
