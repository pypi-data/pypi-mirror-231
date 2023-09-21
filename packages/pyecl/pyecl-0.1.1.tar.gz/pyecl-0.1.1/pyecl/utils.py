import datetime
import hashlib


def constellation_date_string(dt):
    """Return a datetime formatted in the format constellation
    wants as a string like: 2021-02-17T15:16:36Z

    Note - the datetime object must be in utc time."""
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def constellation_date_from_string(date_string):
    """Return a datetime object from the string format that constellation
    uses like: 2021-02-09T04:12:02.618767Z

    Note - the datetime object will be in utc time."""
    # Handle both second and subsecond precision on datetimes
    try:
        return datetime.datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%fZ")
    except ValueError:
        pass

    return datetime.datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%SZ")


def parts_to_xml(parts):
    part_nodes = "\n".join(
        f"""
        <Part>
            <ETag>{part["ETag"]}</ETag>
            <PartNumber>{part["PartNumber"]}</PartNumber>
        </Part>
        """
        for part in parts
    )

    xml = f"""
        <?xml version="1.0" encoding="UTF-8"?>
        <CompleteMultipartUpload xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
        {part_nodes}
        "</CompleteMultipartUpload>"
    """

    return xml.encode("ascii")


def md5_hash_file(file_path):
    with open(file_path, "rb") as file:
        chunk_size = 1_000_000  # 1MB, a bit arbitrary
        md5 = hashlib.md5()
        chunk = file.read(chunk_size)
        while chunk:
            md5.update(chunk)
            chunk = file.read(chunk_size)
        return md5
