from mamba import description, context, it
from expects import expect, equal
from trivia import Game

with description('Trivia') as self:
    with it('foo'):
        g = Game()
        
        expect(True).to(equal(True))