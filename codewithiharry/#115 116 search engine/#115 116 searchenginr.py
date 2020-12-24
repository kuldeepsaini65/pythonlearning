def findingMatches(query, data):
    matched = 0  # This is a Score  of Keyword Matched with Query
    # it Will Increase When Matched it will help to Short results

    word_of_query = query.split(' ')  # these lines will split all word to match with words of data stored
    word_of_data = data.split(' ')

    for words1 in word_of_query:
        for words2 in word_of_data:
            # print(f'Matching Word {words1} With {words2}')
            if words1.lower() == words2.lower():  # this will convert all upper in lower and then match
                matched += 1   # increase score to sort it by higher matched keyword

    return matched


if __name__ == '__main__':
    data = ['kuldeep is learning python', 'python', 'python is popular language', 'what is python', 'saini ji']

    query = input('Please Enter your Query Here:- ')

    scores_of_matched = [findingMatches(query, datas) for datas in data] # it help to print number of matched keyword

    # print(scores_of_matched)
    sorted_sentence_score = [sentscore for sentscore in sorted(zip(scores_of_matched, data), reverse=True)]  # this will help to short by number of higher matches
    print('\n')

    for number, items in sorted_sentence_score: # now avoiding number of matched keyword and printing results after shorting
        print(items)