import re


to_snake_case = lambda __s=str(): re.sub(r"(?<!^)(?=[A-Z])", '_', str(__s)).lower()
to_camel_case = lambda __s=str(): ''.join([s.capitalize() if __i > 0 else s for __i, s in enumerate(str(__s).split('_'))])


def exists_context(**context):
    return {key: value for key, value in context.items() if value or isinstance(value, (bool,float,int))}


UNIQUE_CONTEXT = lambda self=None, asyncio=None, operation=None, host=None, where=None, which=None, \
                        initTime=None, contextFields=None, iterateArgs=None, iterateProduct=None, \
                        pagination=None, pageUnit=None, pageLimit=None, responseType=None, \
                        debug=None, localSave=None, extraSave=None, interrupt=None, \
                        logger=None, logJson=None, errors=None, renameMap=None, schemaInfo=None, \
                        redirectArgs=None, redirectProduct=None, maxLimit=None, redirectLimit=None, \
                        crawler=None, authClass=None, dependencies=None, \
                        self_var=None, prefix=None, rename=None, **context: context


TASK_CONTEXT = lambda locals=None, how=None, default=None, dropna=None, strict=None, unique=None, \
                        index=None, **context: UNIQUE_CONTEXT(**context)


REQUEST_CONTEXT = lambda session=None, semaphore=None, method=None, url=None, referer=None, messages=None, \
                        params=None, encode=None, data=None, json=None, headers=None, allow_redirects=None, \
                        close=None, verify=None, validate=None, exception=None, valid=None, invalid=None, \
                        html=None, table_header=None, table_idx=None, engine=None, how=None, default=None, \
                        dropna=None, strict=None, unique=None, **context: TASK_CONTEXT(**context)


RESPONSE_CONTEXT = lambda iterateUnit=None, fromNow=None, logName=None, logLevel=None, logFile=None, \
                        delay=None, progress=None, message=None, numTasks=None, \
                        apiRedirect=None, redirectUnit=None, encryptedKey=None, \
                        cookies=None, **context: REQUEST_CONTEXT(**context)


UPLOAD_CONTEXT = lambda key=None, sheet=None, mode=None, base_sheet=None, cell=None, \
                        table=None, project_id=None, schema=None, progress=None, \
                        partition=None, prtition_by=None, base=None, **context: context


PROXY_CONTEXT = lambda fields=list(), iterateUnit=0, interval=None, fromNow=None, \
                        startDate=None, endDate=None, datetimeUnit=str(), tzinfo=None, returnType=None, \
                        logName=str(), logLevel=str(), logFile=str(), \
                        delay=0., progress=True, message=str(), numTasks=0, \
                        apiRedirect=False, redirectUnit=0, queryInfo=None, uploadInfo=None, \
                        encryptedKey=None, decryptedKey=None, cookies=str(), **context: \
    dict(exists_context(
        fields = fields,
        iterateUnit = iterateUnit,
        interval = interval,
        fromNow = fromNow,
        startDate = startDate,
        endDate = endDate,
        datetimeUnit = datetimeUnit,
        tzinfo = tzinfo,
        returnType = returnType,
        logName = logName,
        logLevel = logLevel,
        logFile = logFile,
        delay = delay,
        numTasks = numTasks,
        progress = progress,
        message = message,
        apiRedirect = apiRedirect,
        redirectUnit = redirectUnit,
        encryptedKey = encryptedKey,
        cookies = cookies,
        ), **context)


REDIRECT_CONTEXT = lambda apiRedirect=None, returnType=None, renameMap=None, logFile=None, **context: \
    PROXY_CONTEXT(**REQUEST_CONTEXT(**context))
