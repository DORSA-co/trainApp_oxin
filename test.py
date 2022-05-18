from tenacity import retry,stop_after_attempt


@retry(stop=stop_after_attempt(1000))
def raise_my_exception():
    raise "Fail"

try:
    raise_my_exception()
except Exception:
    pass

print(raise_my_exception.retry.statistics)