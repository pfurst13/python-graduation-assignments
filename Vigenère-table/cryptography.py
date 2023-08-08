class Crypto:

    def __init__(self, concanate_keyword, coding_table):
        self.concanate_keyword = concanate_keyword
        self.coding_table = coding_table

    def coded_text(self, formated_user_text):
        final_result = ""
        for i in range(len(formated_user_text)):
            column = 0
            row = 0
            for j, line in enumerate(self.coding_table):
                if line[0] == formated_user_text[i]:
                    column = j
                    row = self.coding_table[0].index(self.concanate_keyword[i])
                final_result.join(self.coding_table[column][row])
        return final_result