
fn number(bus_stops: &[(i32,i32)]) -> i32 {
    // 1 - 5, 2 -> 3
    // 2 - 10, 3 -> 3 + 7
    // 3 - 2, 11 -> 10 - 9

    bus_stops
        .iter()
        .fold(0, |a, n| {
            a + (n.0 - n.1)
        })
}

#[test]
fn returns_expected() {
    assert_eq!(number(&[(10,0),(3,5),(5,8)]), 5);
    assert_eq!(number(&[(3,0),(9,1),(4,10),(12,2),(6,1),(7,10)]), 17);
    assert_eq!(number(&[(3,0),(9,1),(4,8),(12,2),(6,1),(7,8)]), 21);
}
