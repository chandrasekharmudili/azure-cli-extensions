# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import

helps['storage blob copy start'] = """
type: command
short-summary: List blobs in a given container.
parameters:
  - name: --source-uri -u
    type: string
    short-summary: >
        A URL of up to 2 KB in length that specifies an Azure file or blob.
        The value should be URL-encoded as it would appear in a request URI.
        If the source is in another account, the source must either be public
        or must be authenticated via a shared access signature. If the source
        is public, no authentication is required.
        Examples:
        `https://myaccount.blob.core.windows.net/mycontainer/myblob`,
        `https://myaccount.blob.core.windows.net/mycontainer/myblob?snapshot=<DateTime>`,
        `https://otheraccount.blob.core.windows.net/mycontainer/myblob?sastoken`
  - name: --destination-if-modified-since
    type: string
    short-summary: >
        A DateTime value. Azure expects the date value passed in to be UTC.
        If timezone is included, any non-UTC datetimes will be converted to UTC.
        If a date is passed in without timezone info, it is assumed to be UTC.
        Specify this conditional header to copy the blob only
        if the destination blob has been modified since the specified date/time.
        If the destination blob has not been modified, the Blob service returns
        status code 412 (Precondition Failed).
  - name: --destination-if-unmodified-since
    type: string
    short-summary: >
        A DateTime value. Azure expects the date value passed in to be UTC.
        If timezone is included, any non-UTC datetimes will be converted to UTC.
        If a date is passed in without timezone info, it is assumed to be UTC.
        Specify this conditional header to copy the blob only
        if the destination blob has not been modified since the specified
        date/time. If the destination blob has been modified, the Blob service
        returns status code 412 (Precondition Failed).
  - name: --source-if-modified-since
    type: string
    short-summary: >
        A DateTime value. Azure expects the date value passed in to be UTC.
        If timezone is included, any non-UTC datetimes will be converted to UTC.
        If a date is passed in without timezone info, it is assumed to be UTC.
        Specify this conditional header to copy the blob only if the source
        blob has been modified since the specified date/time.
  - name: --source-if-unmodified-since
    type: string
    short-summary: >
        A DateTime value. Azure expects the date value passed in to be UTC.
        If timezone is included, any non-UTC datetimes will be converted to UTC.
        If a date is passed in without timezone info, it is assumed to be UTC.
        Specify this conditional header to copy the blob only if the source blob
        has not been modified since the specified date/time.
examples:
  - name: Copy a blob asynchronously. Use `az storage blob show` to check the status of the blobs.
    text: |
        az storage blob copy start --account-key 00000000 --account-name MyAccount --destination-blob MyDestinationBlob --destination-container MyDestinationContainer --source-uri https://storage.blob.core.windows.net/photos
  - name: Copy a blob asynchronously. Use `az storage blob show` to check the status of the blobs.
    text: |
        az storage blob copy start --account-name MyAccount --destination-blob MyDestinationBlob --destination-container MyDestinationContainer --sas-token $sas --source-uri https://storage.blob.core.windows.net/photos
"""

helps['storage blob download'] = """
type: command
short-summary: Download a blob to a file path, with automatic chunking and progress notifications.
"""

helps['storage blob filter'] = """
type: command
short-summary: List blobs across all containers whose tags match a given search expression.
long-summary: >
    Filter blobs searches across all containers within a storage account but can be scoped within the expression to
    a single container.
parameters:
  - name: --tag-filter
    short-summary: >
            The expression to find blobs whose tags matches the specified condition.
            eg. ""yourtagname"='firsttag' and "yourtagname2"='secondtag'"
            To specify a container, eg. "@container='containerName' and "Name"='C'"
"""

helps['storage blob list'] = """
type: command
short-summary: List blobs in a given container.
examples:
  - name: List all storage blobs in a container whose names start with 'foo'; will match names such as 'foo', 'foobar', and 'foo/bar'
    text: az storage blob list -c MyContainer --prefix foo
"""

helps['storage blob metadata'] = """
type: group
short-summary: Manage blob metadata.
"""

helps['storage blob metadata show'] = """
type: command
short-summary: Return all user-defined metadata for the specified blob or snapshot.
examples:
  - name: Get all user-defined metadata for the specified blob.
    text: az storage blob metadata show -n myblob -c mycontainer --account-name mystorageaccount --account-key 0000-0000
"""

helps['storage blob metadata update'] = """
type: command
short-summary: Set user-defined metadata for the specified blob as one or more name-value pairs.
examples:
  - name:  Set user-defined metadata for the specified blob as one or more name-value pairs.
    text: az storage blob metadata update -n myblob -c mycontainer --metadata a=b c=d
"""

helps['storage blob tag'] = """
type: group
short-summary: Manage blob tags.
"""

helps['storage blob tag list'] = """
type: command
short-summary: Get tags on a blob or specific blob version, or snapshot.
"""

helps['storage blob tag set'] = """
type: command
short-summary: Set tags on a blob or specific blob version, but not snapshot.
long-summary: >
    Each call to this operation replaces all existing tags attached to the blob. To remove all
    tags from the blob, call this operation with no tags set.
"""

helps['storage blob undelete'] = """
type: command
short-summary: Restore soft-deleted blobs or snapshots.
long-summary: >
    Operation will only be successful if used within the specified number of days
    set in the delete retention policy.
examples:
  - name:  Restore soft-deleted blob.
    text: az storage blob undelete -n myblob -c mycontainer --account-name mystorageaccount --account-key 0000-0000
"""

helps['storage blob upload'] = """
type: command
short-summary: Upload a file to a storage blob.
long-summary: Creates a new blob from a file path, or updates the content of an existing blob with automatic chunking and progress notifications.
parameters:
  - name: --type -t
    short-summary: Defaults to 'page' for *.vhd files, or 'block' otherwise.
  - name: --maxsize-condition
    short-summary: The max length in bytes permitted for an append blob.
  - name: --validate-content
    short-summary: Specifies that an MD5 hash shall be calculated for each chunk of the blob and verified by the service when the chunk has arrived.
  - name: --tier
    short-summary: A page blob tier value to set the blob to. The tier correlates to the size of the blob and number of allowed IOPS. This is only applicable to page blobs on premium storage accounts.
examples:
  - name: Upload to a blob.
    text: az storage blob upload -f /path/to/file -c mycontainer -n MyBlob
  - name: Upload to a blob with blob sas url.
    text: az storage blob upload -f /path/to/file --blob-url https://mystorageaccount.blob.core.windows.net/mycontainer/myblob?sv=2019-02-02&st=2020-12-22T07%3A07%3A29Z&se=2020-12-23T07%3A07%3A29Z&sr=b&sp=racw&sig=redacted
    text: |
        az storage blob upload --account-name mystorageaccount --account-key 0000-0000 --container-name mycontainer --file /path/to/file --name myblob
    crafted: true
"""