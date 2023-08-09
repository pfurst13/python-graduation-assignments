class Crypto:

    def __init__(self, keyword, coding_table):
        self.keyword = keyword
        self.coding_table = coding_table

    def keyword_format(self,formated_user_text):

        keyword = ""
        for i in range(len(formated_user_text)):
            keyword += self.keyword

        keyword = keyword[:len(formated_user_text)]
        print(keyword)

        return keyword

    def coded_text(self, formated_user_text):

        concatenated_keyword = self.keyword_format(formated_user_text)

        final_list = []
        for i in range(len(formated_user_text)):
            column = 0
            row = 0
            for j, line in enumerate(self.coding_table):
                if line[0] == formated_user_text[i]:
                    column = j
            row = self.coding_table[0].index(concatenated_keyword[i])
            final_list.append(self.coding_table[column][row])
        
        final_result = "".join(final_list)
        return final_result

    def decode_text(self, encoded_user_text):

        concatenated_keyword = self.keyword_format(encoded_user_text)
        final_text = []

        for i in range(len(concatenated_keyword)):
            column = self.coding_table[0].index(concatenated_keyword[i])

            for j, line in enumerate(self.coding_table):
                if line[column] == encoded_user_text[i]:
                    row = j
                    final_text.append(self.coding_table[j][0])
        
        return "".join(final_text)


