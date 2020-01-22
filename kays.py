def makeKeys(l):
  return {
    "consumerAPIKey": l[0],
    "consumerAPISecretKey": l[1],
    "accessToken": l[2],
    "accessTokenSecret": l[3]
  }

appKeys = list(map(makeKeys, [
  ["jIKiVc6tRLGMXf3lzMqSWHJ9u", "53LESyUrtO8CxmVW9tGupHdz8ac0eD5dlMKvCZOAaL8rEym9qL", "796229025815523328-Zzs0OrYstjcAaaoz59EVufwr2SC2yAn", "9Ia0tUL7PRqF6XtogfWM1eBEHYlFVlrG5EkPvduguLGQx"],
  ["GFfcfWaCpTlvOy0GS9MzuHJNS", "OuFB09twPEwfMtJKWhVdvxjHceaaBrgvwG62dclXVQbDxBC4Fo", "796229025815523328-QPMsfvdCMs7Bn3ZE0MiuMPfjGAScTe9", "IUCpq55hfPMqbOa3AzI0hiZRggEicYDa10nkEUZC1RqV8"],
  ["3cRovJYsSH9FnuS7Igh6EZO6X", "XPxZm0M31y4E86xGN40lglizkBs4wQcapS02UsWLbWoZc8c8we", "796229025815523328-6AxFFCxNuCHVv4S10pdAufeaRSWkLJo", "FJFTw8FFjwEAOo6pkwG5gTlxLa7Qc0JjFGnvH4fHoOHCG"]
]))
