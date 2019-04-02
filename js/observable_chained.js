const { range } = require('rxjs');
const { map, filter } = require('rxjs/operators');

range(1, 10).pipe(
  filter(x => x % 2 === 1),
  map(x => x + 1 ),
  map(x2 => x2 + 2),
  filter(x3 => x3 % 4 === 0)
).subscribe(y => console.log(y));
