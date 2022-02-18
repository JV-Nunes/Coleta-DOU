
class GetDou:
    def __init__(self):
        pass

    def extract_section_1(self, df, date):
        df=df[df['data_publicacao']==date]
        if (len(df) != 0):
            return df
        else: 
            print("We still don't have this day's publication!")
            return -1

    def extract_filtered_section1(self, df, date, filter):
        df=df[df['data_publicacao']==date]
        if (len(df) != 0):
            return df[df['titulo'].str.contains(filter, regex=True, na=False)] 
        else:
            print("We still don't have this day's publication!")
            return -1 