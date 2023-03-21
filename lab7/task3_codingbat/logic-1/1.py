def cigar_party(cigars, is_weekend):
  if cigars>=40:
    if is_weekend ==True:
      return True
    else:
      if cigars<=60:
        return True
  return False