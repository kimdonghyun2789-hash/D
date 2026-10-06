# Path configuration — everything is resolved relative to the repository root.
import os
DECK = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(DECK, '..', '..'))
RENDERS = os.path.join(ROOT, 'assets', 'renders') + os.sep
ORIGINAL = os.path.join(ROOT, 'assets', 'original') + os.sep
MODEL_JSON = os.path.join(DECK, 'model.json')
TEMPLATE = os.path.join(DECK, 'template_original.pptx')
OUTPUT = os.path.join(ROOT, 'SoftHand_Founding_Seed_IR_Deck_Final.pptx')
