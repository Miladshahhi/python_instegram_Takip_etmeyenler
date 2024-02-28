import instaloader

iceri_al = instaloader.Instaloader()

username = "kullanıcıAdı"
password = "Şifreniz"
iceri_al.login(username, password)  # (login)

profile = instaloader.Profile.from_username(L.context, username)

# Takipçileri al
followers_file = "takipci.txt"
with open(followers_file, "w") as f:
    for follower in profile.get_followers():
        f.write(follower.username + '\n')
    print("Takipçiler yazıldı.")

# Takip edilenleri al
followees_file = "takipedilen.txt"
with open(followees_file, "w") as f:
    for followee in profile.get_followees():
        f.write(followee.username + '\n')
    print("Takip edilenler yazıldı.")

# Takip etmeyenleri bul
followers_set = set(open(followers_file).readlines())
followees_set = set(open(followees_file).readlines())

unfollowers_set = followees_set.difference(followers_set)

# Takip etmeyenleri txt dosyasına yaz
unfollowers_file = "takip_etmeyenler.txt"
with open(unfollowers_file, "w") as f:
    for unfollower in unfollowers_set:
        f.write(unfollower)
    print("Takip etmeyenler dosyaya yazıldı.")
