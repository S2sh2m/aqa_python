def balck_sea(black_sea_square=436402, azov_sea_square=37800):
    azov_and_black = black_sea_square + azov_sea_square
    return azov_and_black

def warehouse(all_warehouse=375291, first_and_second=250449, second_and_third=222950):
    first = all_warehouse - second_and_third
    third = all_warehouse - first_and_second
    second = all_warehouse - (first + third)
    return first, second, third

def payment(month_pay=1179, pay_term=18):
    pc_price = month_pay * pay_term
    return pc_price