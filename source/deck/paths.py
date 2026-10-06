import os
DECK = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(DECK, '..', '..'))
RAW = os.path.join(ROOT, 'assets', 'renders', 'raw')        # 3D renders as rendered (scene background kept)
RENDERS = os.path.join(ROOT, 'assets', 'renders')           # trimmed transparent cut-outs (hand, screwdriver)
ORIGINAL = os.path.join(ROOT, 'assets', 'original')         # images kept from the original deck
MODEL_JSON = os.path.join(DECK, 'model.json')
OUTPUT = os.path.join(ROOT, 'SoftHand_Founding_Seed_IR_Deck_Final.pptx')
PREVIEW = os.path.join(ROOT, 'SoftHand_Founding_Seed_IR_Deck_Final_preview.pdf')
