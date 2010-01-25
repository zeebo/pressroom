
def sha(data=None, len=0):
  if data is None:
    data = random.random()
      
  digest = hashlib.sha1(str(data)).hexdigest()
  if len == 0:
    return digest
  return digest[:len]