import pandas

squirrel_data = pandas.read_csv("squirrel_data.csv")

# New CSV with only: Fur Color, Count
squirrel_fur_color = ["grey", "cinnamon", "black"]

squirrel_count_grey = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
squirrel_count_red = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
squirrel_count_black = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

squirrel_count_colors = [squirrel_count_grey, squirrel_count_red, squirrel_count_black]

squirrel_data_dict = {
    "Fur Color": squirrel_fur_color,
    "Count": squirrel_count_colors
}

squirrel_data_frame = pandas.DataFrame(squirrel_data_dict)

squirrel_data_frame.to_csv("squirrel_count.csv")