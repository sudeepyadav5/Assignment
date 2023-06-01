class RecentlyPlayedStore:
    def __init__(self, capacity):
        self.capacity = capacity
        self.store = {}

    def play_song(self, user, song):
        if user not in self.store:
            self.store[user] = []
        elif song in self.store[user]:
            self.store[user].remove(song)
        elif len(self.store[user]) >= self.capacity:
            self.store[user].pop(0)

        self.store[user].append(song)

    def get_recently_played(self, user):
        if user in self.store:
            return self.store[user]
        else:
            return []


# Example usage
store = RecentlyPlayedStore(3)
store.play_song("User", "Song1")
store.play_song("User", "Song2")
store.play_song("User", "Song3")
print(store.get_recently_played("User"))  # Output: ['Song1', 'Song2', 'Song3']
store.play_song("User", "Song4")
print(store.get_recently_played("User"))  # Output: ['Song2', 'Song3', 'Song4']
store.play_song("User", "Song2")
print(store.get_recently_played("User"))  # Output: ['Song3', 'Song4', 'Song2']
store.play_song("User", "Song1")
print(store.get_recently_played("User"))  # Output: ['Song4', 'Song2', 'Song1']
