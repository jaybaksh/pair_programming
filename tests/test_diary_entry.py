from lib.diary_entry import*
#def test_check_class_intialisation():
#    actual.title = DiaryEntry("Harry Potter", "Chapter 1")
#    actual.contents = DiaryEntry.contents
#
#    expected_title = "Harry Potter"
#    expected_contents = "Chapter 1"
#
#    assert actual.title == expected_title
#    assert actual.contents == expected_contents

#scenario 1: is the diary entry formatted
def test_format_diarytitle_content():
    title = "Harry Potter"
    contents = "chapter 1"
    assert f"{title}: {contents}" == "Harry Potter: chapter 1"

def test_count_entry():
    diary_entry = DiaryEntry('Monday', 'Hello world hello world hello world')
    assert diary_entry.count_words() == 6

#scenario 3: check if the given WPM returns a reading time
def test_reading_time():
    diary_entry = DiaryEntry('Monday', 'Hello world hello world hello world')
    wpm = diary_entry.reading_time(200.0)
    assert wpm == 0.03

#Scenario 4: reading_chunk called once
def test_reading_chunk_once():
    diary_entry = DiaryEntry('Monday', 'Hello world hello world hello world')
    result = diary_entry.reading_chunk(3,1)
    assert result == "Hello world hello"

#Scenario 5: reading_chunk called twice
def test_reading_chunk_twice():
    diary_entry = DiaryEntry('Monday', 'Hello world hello world hello world')
    assert diary_entry.reading_chunk(3,1) == "Hello world hello"
    assert diary_entry.reading_chunk(3,1) == "world hello world"


#Scenario 6: Reading_chunk called multiple times repeating the chunk from beginning
def test_reading_chunk_multiplt():
    diary_entry = DiaryEntry('Monday', 'Hello world hello world hello world')
    assert diary_entry.reading_chunk(3,1) == "Hello world hello"
    assert diary_entry.reading_chunk(2,1) == "world hello"
    assert diary_entry.reading_chunk(3,1) == "world"
    assert diary_entry.reading_chunk(2,2) == "Hello world hello world"