from groundx.paths.v1_bucket_bucket_id.get import ApiForget
from groundx.paths.v1_bucket_bucket_id.put import ApiForput
from groundx.paths.v1_bucket_bucket_id.delete import ApiFordelete


class V1BucketBucketId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
