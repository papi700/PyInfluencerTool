from package.api.sheet import *


def get_influencer_data_by_username(username) :
    if is_in_col(username, 1) :
        datas = get_row_values(username)
        influencer = Influencer(datas)
        return influencer
    else :
        return None


def get_influencers_by_followers(min, max) :
    list = []
    followers_numbers = get_col_values("FOLLOWERS")
    for i in range(len(followers_numbers)) :
        if followers_numbers[i] != "FOLLOWERS" :
            followers_numbers[i] = in_int(followers_numbers[i])
            if min <= followers_numbers[i] <= max :
                list.append(get_cell_value_from_index(i, 1))
    return list


def get_influencers_by_engagement_rate(min, max) :
    list = []
    engagement_rates = get_col_values("E.R")
    for i in range(len(engagement_rates)) :
        if engagement_rates != "E.R" :
            engagement_rates[i] = float(engagement_rates[i].replace("%", ""))
            if min <= engagement_rates[i] <= max :
                list.append(get_cell_value_from_index(i, 1))
    return list


def get_available_countries() :
    available_countries = get_col_values("COUNTRY")
    available_countries.remove("COUNTRY")
    return available_countries


def get_influencers_with_email_address() :
    list = []
    email_addresses = get_col_values("MAIL")
    for i in range(len(email_addresses)) :
        if email_addresses[i] != "MAIL" and email_addresses[i] != "" :
            list.append(get_cell_value_from_index(i, 1))
    return list


def get_influencers_contacted_by(contacting_means) :
    list = []
    all_contacting_means = get_col_values("CONTACTED BY")
    for i in range(len(all_contacting_means)) :
        if all_contacting_means[i] != "CONTACTED BY" and all_contacting_means[i] == contacting_means :
            list.append(get_cell_value_from_index(i, 1))
    return list


def get_all_influencers() :
    list = []
    all_usernames = get_col_values("USERNAME")
    for i in range(len(all_usernames)) :
        if all_usernames[i] != "USERNAME" :
            list.append(get_cell_value_from_index(i, 1))
    return list


class Influencer :
    def __init__(self, datas="") :
        self.set_all_attributes(datas)

    def set_all_attributes(self, values) :
        attributes = ["username", "followers", "engagement_rate", "country", "name", "mail", "contacted_by",
                      "DM_response_time", "email_response_time", "deal_offer", "story_views",
                      "swipeup_link_clicks", "conversion_rate", "generated_turnover",
                      "generated_followers"]
        if values == "" :
            for attribute in attributes :
                setattr(self, attribute, values)
        else :
            for (value, attribute) in zip(values, attributes) :
                setattr(self, attribute, value)

    def is_in_list(self) :
        return is_in_col(self.username, 1)

    def get_datas_to_add(self) :
        datas_to_add = []
        datas_and_columns_tuples = self.link_datas_to_columns()
        if self.is_in_list() :
            influencer_datas_list = get_row_values(self.username)
            for i in range(1, len(datas_and_columns_tuples)) :
                if i < len(influencer_datas_list) - 1 :
                    influencer_datas_list.append("")
                if datas_and_columns_tuples[i][0] != influencer_datas_list[i] :
                    datas_to_add.append(datas_and_columns_tuples[i])
            return datas_to_add
        else :
            return datas_and_columns_tuples

    def add_datas(self) :
        datas = self.get_datas_to_add()
        if datas != [] :
            datas_and_columns_tuples = self.link_datas_to_columns()
            if len(datas) != len(datas_and_columns_tuples) :
                cell = sheet.find(self.username)
                row = cell.row
            else :
                row = get_last_row() + 1
            add_to_sheet(row, datas)

    def link_datas_to_columns(self) :
        data = [(self.username, 1), (self.followers, 2), (self.engagement_rate, 3),
                (self.country, 4), (self.name, 5), (self.mail, 6), (self.contacted_by, 7),
                (self.DM_response_time, 8), (self.email_response_time, 9),
                (self.deal_offer, 10), (self.story_views, 11), (self.swipeup_link_clicks, 12),
                (self.conversion_rate, 13), (self.generated_turnover, 14), (self.generated_followers, 15)]
        return data


if __name__ == '__main__' :
   pass