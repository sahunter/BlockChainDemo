import datetime as date
import Block

def create_genesis_block():
    #Manually construct a block with
    # index zero and arbitrary previous hash
    return Block.Block(0,date.datetime.now(),"Genesis Block","0")

# def main():
#     create_genesis_block()
# if __name__ == '__main__':
#     main()
