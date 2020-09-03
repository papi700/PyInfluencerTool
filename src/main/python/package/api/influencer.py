import smtplib
from email.message import EmailMessage
import json

from package.api.sheet import *
from package.api.constants import SERVER_LOGIN, SERVER_PASSWORD


def get_influencer_data_by_username(username) :
    if is_in_col(username, 1) :
        datas = get_row_values(username)
        influencer = Influencer(datas)
        return influencer
    else :
        return None


def get_influencers_by_followers(min, max) :
    final_list = []
    followers_numbers = get_col_values("FOLLOWERS")
    # print(followers_numbers)
    for i in range(len(followers_numbers)) :
        if followers_numbers[i] != "":
            followers_numbers[i] = in_int(followers_numbers[i])
            # print(min, " ", followers_numbers[i], " ", max)
            if min <= followers_numbers[i] <= max :
                final_list.append(get_cell_value_from_index(i, 1))
    # print(list)
    return final_list


def get_influencers_by_engagement_rate(min, max) :
    final_list = []
    engagement_rates = get_col_values("E.R")
    for i in range(len(engagement_rates)) :
        if engagement_rates[i] != "":
            current_engagement_rate = float(engagement_rates[i].replace("%", ""))
            if min <= current_engagement_rate <= max :
                final_list.append(get_cell_value_from_index(i, 1))
    return final_list


def get_available_countries() :
    available_countries = get_col_values("COUNTRY")
    available_countries = list(filter(None, available_countries))
    for country in available_countries :
        if available_countries.count(country) > 1 :
            available_countries.remove(country)
    return available_countries


def get_influencers_by_country(country_name) :
    final_list = []
    all_countries = get_col_values("COUNTRY")
    for i in range(len(all_countries)) :
        if all_countries[i] == country_name :
            final_list.append(get_cell_value_from_index(i, 1))
    return final_list


def get_influencers_with_email_address() :
    final_list = []
    email_addresses = get_col_values("MAIL")
    for i in range(len(email_addresses)) :
        if email_addresses != "":
            final_list.append(get_cell_value_from_index(i, 1))
    return email_addresses


def get_influencers_contacted_by(contacting_means) :
    final_list = []
    all_contacting_means = get_col_values("CONTACTED BY")
    all_contacting_means = list(filter(None, all_contacting_means))
    for i in range(len(all_contacting_means)) :
        if all_contacting_means[i] == contacting_means :
            final_list.append(get_cell_value_from_index(i, 1))
    return final_list


def get_all_influencers() :
    list = []
    all_usernames = get_col_values("USERNAME")
    for i in range(len(all_usernames)) :
        if all_usernames[i] != "USERNAME" :
            list.append(get_cell_value_from_index(i, 1))
    return list


def email_influencer(influencer_username, selected_template) :
    i = get_influencer_data_by_username(influencer_username)
    if i.contacted_by == "DM_only" or i.contacted_by == "not yet" :
        values = [i.username, i.followers, i.engagement_rate, i.country, i.name, i.mail]
        mail_subject = selected_template.replace_variables_in("subject", values)
        mail_body = selected_template.replace_variables_in("body", values)
        mail = EmailMessage()
        mail['Subject'] = mail_subject
        mail['From'] = SERVER_LOGIN
        mail['To'] = i.mail
        mail.set_content(mail_body)
        with smtplib.SMTP('smtp-relay.sendinblue.com', 587) as smtp :
            smtp.login(SERVER_LOGIN, SERVER_PASSWORD)
            smtp.send_message(mail)
        if i.contacted_by == "not yet" :
            i.contacted_by = "mail only"
            i.add_datas()
        else :
            i.contacted_by = "DM and mail"
            i.add_datas()


class EmailError(Exception) :
    pass


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
            for i in range(len(attributes)) :
                if i <= len(values) - 1 :
                    setattr(self, attributes[i], values[i])
                else :
                    setattr(self, attributes[i], "")

    def is_in_list(self) :
        return is_in_col(self.username, 1)

    def get_datas_to_add(self) :
        datas_to_add = []
        datas_and_columns_tuples = self.link_datas_to_columns()
        if self.is_in_list() :
            influencer_datas_list = get_row_values(self.username)
            for i in range(1, len(datas_and_columns_tuples)) :
                value = datas_and_columns_tuples[i][0]
                if i > len(influencer_datas_list) - 1 :
                    influencer_datas_list.append("")
                data = influencer_datas_list[i]
                if not value in ("", data) :
                    for data_and_column in datas_and_columns_tuples :
                        if value in data_and_column :
                            column = data_and_column[0]
                    if "%" in value and float(value.replace("%", "")) != float(data.replace("%", "")) :
                        datas_to_add.append((column, value))
                    elif not "%" in value :
                        datas_to_add.append((column, value))
            return datas_to_add
        else :
            if self.mail != "" and is_in_col(self.mail, 6) :
                raise EmailError
                # print("is in")
            else :
                return datas_and_columns_tuples

    def add_datas(self) :
        datas = self.get_datas_to_add()
        if datas != [] :
            datas_and_columns_tuples = self.link_datas_to_columns()
            if len(datas) != len(datas_and_columns_tuples) :
                cell = SHEET.find(self.username)
                print(self.username)
                row = cell.row
            else :
                row = get_last_row() + 1
            add_to_sheet(row, datas)
            return True
        else :
            return None

    def link_datas_to_columns(self) :
        data = []
        all_datas = self.__dict__
        keys = self.__dict__.keys()
        i = 1
        for key in keys :
            data.append((i, all_datas.get(key)))
            i += 1
        return data


if __name__ == '__main__' :
    # ts = get_templates()
    # for t in ts:
    #     if t.name == "template_2":
    #         st = t
    # email_influencer("papiee75", st)
    # i = get_influencer_data_by_username("papiee75")
    # print(i.link_datas_to_columns())
    # print(get_influencers_by_followers(12000, 40000))
    pass
