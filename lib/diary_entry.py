class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.wordcount = len(contents.split())
        self.words = self.contents.split()
        self.startingpoint = 0
        

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        diary_entry_list = self.contents.split()
        diary_entry_count = len(diary_entry_list)
        return diary_entry_count

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        return self.wordcount/wpm

    def reading_chunk(self, wpm, minutes):
        reading_capacity = wpm * minutes
        if self.startingpoint > len(self.words):
            self.startingpoint = 0
        start = self.startingpoint 
        end = start + reading_capacity
        read = self.words[start:end]
        self.startingpoint = end
        return " ".join(read)
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        