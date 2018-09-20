from mamba import description, context, it
from expects import expect, equal,be
from trivia import Game

import io
import sys


with description('Trivia') as self:
    with before.each:
        self.g = Game()
        self.g.add('u1')
        self.g.add('u2')
        self.g.add('u3')

    with it('initial player is 0'):
        expect(self.g.current_player).to(equal(0))
        expect(self.g.players).to(equal(['u1','u2','u3']))
        expect(self.g.places).to(equal([0,0,0,0,0,0]))
        expect(self.g.purses).to(equal([0,0,0,0,0,0]))
    
    with it('roll'):
        f = io.StringIO()
        self._stdout = sys.stdout
        sys.stdout = f
        
        self.g.roll(4)
        
        self.g.roll(4)
        sys.stdout = self._stdout

        print("EFA", f.read())
        expect(self.g.current_player).to(equal(0))