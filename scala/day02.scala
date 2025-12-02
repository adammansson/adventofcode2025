//> using toolkit default

def base(pred: String => Boolean): Long =
  os.read(os.pwd / "input" / "day02" / "in.txt")
    .strip
    .split(",")
    .map(_.trim)
    .collect { case s"$start-$end" => start.toLong to end.toLong }
    .flatMap(range =>
      range.view
        .map(_.toString)
        .filter(pred)
        .map(_.toLong)
    )
    .sum

def partOne(): Long =
  base(s =>
    val mid = s.length / 2
    s.length % 2 == 0 && s.take(mid) == s.drop(mid)
  )

def partTwo(): Long =
  base(s =>
    (1 to s.length / 2)
      .filter(gs => s.length % gs == 0)
      .exists(gs =>
        val seq = s.take(gs)
        s.grouped(gs).forall(_ == seq)
      )
  )

@main def run(): Unit =
  println(partOne())
  println(partTwo())
