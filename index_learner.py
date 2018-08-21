
def learn_index(num_datapoints,x,model,learning_rate = 1e-2): 
    #np_data
    #model (untrained)
    import torch
    import numpy as np
    N, D_in, H, D_out = 64, 1, 100, 1
    #x = torch.FloatTensor(np_data.reshape(num_datapoints,1)[:,:])
    y = torch.FloatTensor(np.arange(num_datapoints).reshape(num_datapoints,1))
    if model is None:
        model = torch.nn.Sequential(
            torch.nn.Linear(D_in, H),
            torch.nn.ReLU(),
            torch.nn.Linear(H, D_out),
        )
    loss_fn = torch.nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    plot_step,plot_lossess = [],[]
    for t in range(5000):
        y_pred = model(x)


        loss = loss_fn(y_pred, y)
        if t%1000 == 0:
            print(t, loss.item())
            plot_step.append(t)
            plot_lossess.append(loss.item())


        optimizer.zero_grad()


        loss.backward()


        optimizer.step()
    return plot_step,plot_lossess,model

        
def predict_indexes(num_datapoints,model,x):
    #num_datapoints
    #model
    #x
    error_predicted_index = []
    predicted_index = []
    for p in range(0,num_datapoints-1):
        p_i = model(x[p])
        predicted_index.append(p_i)
        error_predicted_index.append(p_i - p)

    print("Total datapoint: "+str(num_datapoints))
    return predicted_index,error_predicted_index

    
def plot_results(num_datapoints,predicted_index,error_predicted_index
                ,plot_step,plot_lossess,np_data):
    #num_datapoints
    #predicted_index
    #error_predicted_index
    #plot_step
    #plot_lossess
    #np_data
    
    import matplotlib.pyplot as plt
    plt.style.use('seaborn-whitegrid')

    fig = plt.figure(figsize=(20,10))
    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(222)
    ax3 = fig.add_subplot(223)
    ax4 = fig.add_subplot(224)

    ax = ax1
    ax.set_xlabel("actual index",fontsize=15)
    ax.set_ylabel("predicted index",fontsize=15)
    ax.set_title("Plot 1: slope of 45° indicates a high quality index prediction", fontsize=15)
    ax.plot(range(0,num_datapoints-1), predicted_index);

    ax = ax2
    ax.set_xlabel("index",fontsize=15)
    ax.set_ylabel("error",fontsize=15)
    ax.set_title("Plot 2: error in index prediction is mostly around zero except near the start and end", fontsize=15)
    ax.plot(range(0,num_datapoints-1), error_predicted_index);

    ax = ax3
    ax.set_xlabel("number of episodes",fontsize=15)
    ax.set_ylabel("loss",fontsize=15)
    ax.set_title("Plot 3: Training the neural net model. Loss vs training episodes ", fontsize=15)

    ax.plot(plot_step, plot_lossess);

    ax = ax4
    ax.set_xlabel("index",fontsize=15)
    ax.set_ylabel("data point",fontsize=15)
    ax.set_title("Plot 3: The log normal dataset", fontsize=15)
    ax.plot(range(num_datapoints), np_data);