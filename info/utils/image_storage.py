from qiniu import put_data, Auth

access_key = "dphFdb5l7gBLGcwMSe2U4PiJ6xz6Gn8J7c3bAiMl"
secret_key = "s3tIDZV86WmpQZl1wEYsPOI5jqXYXKstyZkmkgQt"
bucket_name = "ihome"


def storage(data):
    try:
        q = Auth(access_key, secret_key)
        token = q.upload_token(bucket_name)
        ret, info = put_data(token, None, data)
        print(ret, info)
    except Exception as e:
        raise e

    if info.status_code != 200:
        raise Exception("上传文件失败")
    return ret["key"]


if __name__ == '__main__':
    file = input("请输入文件路径")
    with open(file, 'rb') as f:
        storage(f.read())