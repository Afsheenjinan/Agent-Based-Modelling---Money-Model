from moneyagent import *
import numpy as np
import matplotlib.pyplot as plt

from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer


##def agent_portrayal(agent):
##    portrayal = {"Shape": "circle",
##                 "Color": "red",
##                 "Filled": "true",
##                 "Layer": 0,
##                 "r": 0.5}
##    return portrayal

def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "r": 0.5}

    if agent.wealth > 0:
        portrayal["Color"] = "red"
        portrayal["Layer"] = 0
    else:
        portrayal["Color"] = "grey"
        portrayal["Layer"] = 1
        portrayal["r"] = 0.2
    return portrayal

grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)

##
##model = MoneyModel(100, 10, 10)
##for i in range(100):
##    model.step()


##gini = model.datacollector.get_model_vars_dataframe()
##print(gini)
##
##agent_wealth = model.datacollector.get_agent_vars_dataframe()
##print(agent_wealth)
##agent_wealth.head()


server = ModularServer(MoneyModel,
                       [grid],
                       "Money Model",
                       {"N":100, "width":10, "height":10})
server.port = 8521 # The default
server.launch()


##gini.plot()
##
##agent_counts = np.zeros((model.grid.width, model.grid.height))
##for cell in model.grid.coord_iter():
##    cell_content, x, y = cell
##    agent_count = len(cell_content)
##    agent_counts[x][y] = agent_count
##plt.imshow(agent_counts, interpolation='nearest')
##plt.colorbar()

# If running from a text editor or IDE, remember you'll need the following:
# plt.show()

