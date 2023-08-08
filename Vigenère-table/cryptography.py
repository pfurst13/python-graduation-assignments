class Crypto:

    def __init__(self, keyword, coding_table):
        self.keyword = keyword
        self.coding_table = coding_table

    def coded_text(self, formated_user_text):

        concanate_keyword = ""
        for i in range(len(formated_user_text)):
            concanate_keyword += formated_user_text

        concanate_keyword = concanate_keyword[:len(formated_user_text)]

        final_list = []
        for i in range(len(formated_user_text)):
            column = 0
            row = 0
            for j, line in enumerate(self.coding_table):
                if line[0] == formated_user_text[i]:
                    column = j
            row = self.coding_table[0].index(concanate_keyword[i])
            final_list.append(self.coding_table[column][row])
        
        final_result = "".join(final_list)
        return final_result