import argparse
from datetime import datetime
import Game
import KnowledgeGraph
import logging
import os

# Logging 
def init_logger():
    folder = "logs"
    filename = f"clue_game{datetime.now().strftime('%Y%m%m_%H%M%S')}"
    os.makedirs(folder, exist_ok=True)
    
    log_file = os.path.join(folder,filename)
    
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    logging.info(f"Log file created: {filename}")
    
# main loop
def main():
    
    parser = argparse.ArgumentParser(description="Run Clue with DEL")
    
    parser.add_argument(
        "--players","-p",
        type=int,
        default=3,
        help="Number of players (default:3)"
    )
    
    parser.add_argument(
        "--runs","-r",
        type=int,
        default=1,
        help="Number of simulation runs, default:1."
    )
    
    args = parser.parse_args()
    
    num_players = args.players
    num_runs = args.runs
    
    init_logger()
    
    for run in range(num_runs):
    
        logging.info(f"Run {run+1}: Simulating CLUE with {num_players} players.")
    
        new_game = Game.Game(num_players=num_players)
        new_game.setup()
        new_game.play()
                
        logging.info("End of simulation.")
        
            
if __name__ == "__main__":
    main()