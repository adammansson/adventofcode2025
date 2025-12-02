//> using toolkit default

def base(f: String => Boolean): Long =
  os.read(os.pwd / "input" / "day02" / "in.txt")
    .strip
    .split(",")
    .map(r => (r.split("-").head).toLong to (r.split("-").last.strip).toLong)
    .map(r => r.filter(n => f(n.toString)).sum)
    .sum

def partOne(): Long =
  base(s => s.take(s.length / 2) == s.drop(s.length / 2))

def partTwo(): Long =
  base(s =>
    (1 to s.length / 2).exists(gs =>
      s.grouped(gs).forall(g => g == s.grouped(gs).next)
    )
  )

@main def run(): Unit =
  println(partOne())
  println(partTwo())
