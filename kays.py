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
  ["3cRovJYsSH9FnuS7Igh6EZO6X", "XPxZm0M31y4E86xGN40lglizkBs4wQcapS02UsWLbWoZc8c8we", "796229025815523328-6AxFFCxNuCHVv4S10pdAufeaRSWkLJo", "FJFTw8FFjwEAOo6pkwG5gTlxLa7Qc0JjFGnvH4fHoOHCG"],
  ["3uqQmfw78NsXYrkb4xe6eE2vS", "SXRgNW973ubNAiOimG8z095W85QUOEYDxuc26JWkCFwGdbbmya", "796229025815523328-ZmTij4r6LZmlGQOaMjZHTr9N65sk9Nv", "ZwDoQW5BqnK7XdQt8vdo5p5gHImqFCQpDVvMqMJgtugp7"],
  ["sa31RZjAu00PFK7QMjz4TCrlL", "4p3h2LIiZOMq7C4Z2XzEo5BJSBqPMPJjklOxbZ4pesjirIwjVz", "796229025815523328-FjEHKh6kzI7MT6nNDg9giUqCuLbmC95", "HUWGB75OhOIxvQdtRd4SHlJBEhyddN8G7Y4C1aTiyruzv"]
]))
