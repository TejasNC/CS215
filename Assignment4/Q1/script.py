def onTimer( 
        best_bid: tuple[int,int],
        best_ask: tuple[int,int],
        your_trades: list[tuple[int,int]],
) -> list[tuple[int,int]]:
    # # Case1: ANomalous bid
    # if best_bid[0] > 100:
    #     return [(best_bid[0], best_bid[1] - 1)]
    # # Case2: Anomalous ask
    # if best_ask[0] < 100:
    #     return [(best_ask[0], best_ask[1] + 1)] 
    # # Case3: Anomalous trade    
    # for trade in your_trades:
    #     if trade[0] > 100:
    #         return [(trade[0], trade[1] - 1)]
    #     if trade[0] < 100:
    #         return [(trade[0], trade[1] + 1)]   
    # return []

    MAX_ORDER_SIZE = 10
    MAX_EXPOSURE = 10
    FAIR_PRICE = 100
    ORDER_LIMIT = 2

    current_exposure = sum([trade[1] for trade in your_trades])
    if abs(current_exposure) >= MAX_EXPOSURE:
        return []
    
    remaining_exposure = MAX_EXPOSURE - abs(current_exposure)

    
    orders = []

    if best_ask[0] < FAIR_PRICE:
        p = best_ask[0] + 1
        return [(p, remaining_exposure)]


    if best_bid[0] > FAIR_PRICE:
        p = best_bid[0] - 1
        return [(p, -1 * remaining_exposure)]

    if ( best_bid[0] - best_ask[0] > 2 ):
        # return [(best_bid[0]-1, max(-1*best_bid[1] + 1,remaining_exposure) ), (best_ask[0]+1, min(-1* best_ask[1] + 1, remaining_exposure))]
        orders.append((best_bid[0]-1, max(-1*best_bid[1] , -1* remaining_exposure) )) # sell
        orders.append( (best_ask[0]+1, min( best_ask[1] , remaining_exposure) )) # buy
        return orders

    
    elif ( best_bid[0] - best_ask[0] > 0 ):
        # return [ ( best_bid[0] , max((-1*best_bid[1] + 1,remaining_exposure))), ( best_ask[0], min(-1 * best_ask[1],remaining_exposure) )]
        orders.append( (best_bid[0], max(-1*best_bid[1] , -1 * remaining_exposure))) # sell
        orders.append( (best_ask[0], min( best_ask[1], remaining_exposure))) # buy
        return orders

    
    if (best_ask[0] > best_bid[0]):
        p = (best_bid[0]*best_ask[1] + best_ask[0]*best_bid[1])//(best_ask[1] + best_bid[1])
        orders.append((p-1, remaining_exposure))
        orders.append((p+1, -1*remaining_exposure))
        return orders
    
    return orders
    # return []


    



    # for trade in your_trades:
    #     if trade[0] > 100:
    #         return [(trade[0], trade[1] - 1)]
    #     if trade[0] < 100:
    #         return [(trade[0], trade[1] + 1)]

