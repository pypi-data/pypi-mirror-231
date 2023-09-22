// Max duration in seconds that can be returned is ~ 136.192519502 years

fn main() {
    // With whitespace
    let time1 = " 00 :00:00";
    let time2 = "00:1 0:00";

    // With seconds
    let time3 = "00:20:00";
    let time4 = "10:00";

    // With milliseconds
    let time5 = "00:20:00:200";
    let time6 = "00:20:00.900";

    let time7 = "20:00:200";
    let time8 = "20:00.200";

    let time9 = "20:hello";

    assert_eq!(parse_to_seconds(time1), Some(0));
    assert_eq!(parse_to_seconds(time2), Some(600));
    assert_eq!(parse_to_seconds(time3), Some(1200));
    assert_eq!(parse_to_seconds(time4), Some(600));
    assert_eq!(parse_to_seconds(time5), Some(1200));
    assert_eq!(parse_to_seconds(time6), Some(1200));
    assert_eq!(parse_to_seconds(time7), Some(1200));
    assert_eq!(parse_to_seconds(time8), Some(1200));
    assert_eq!(parse_to_seconds(time9), None);
}

pub fn parse_to_seconds(time: &str) -> Option<u32> {
    let time = time.replace(" ", "");
    let parts: Vec<&str> = time.split(":").collect();

    match parts.len() {
        1 => {
            // Handle ss case
            let seconds: u32 = parts[0].trim().parse().ok()?;
            return Some(seconds);
        }
        2 => {
            // Handle mm:ss.ms and mm:ss cases
            if parts[1].contains(".") {
                // Assume format is mm:ss.ms
                let minutes: u32 = parts[0].trim().parse().ok()?;
                let seconds: u32 = parts[1].split(".").next()?.trim().parse().ok()?;
                return Some(minutes * 60 + seconds);
            }

            // Assume format is mm:sss
            let minutes: u32 = parts[0].trim().parse().ok()?;
            let seconds: u32 = parts[1].trim().parse().ok()?;
            return Some(minutes * 60 + seconds);
        }
        3 => {
            // Handle hh:mm:ss, mm:ss:ms, hh:mm:ss.ms  cases
            if parts[2].contains(".") {
                // Assume format is hh:mm:ss.ms
                let hours: u32 = parts[0].trim().parse().ok()?;
                let minutes: u32 = parts[1].trim().parse().ok()?;
                let seconds: u32 = parts[2].split(".").next()?.trim().parse().ok()?;
                return Some(hours * 3600 + minutes * 60 + seconds);
            }

            if parts[2].len() <= 2 {
                // Assume format is hh:mm:ss
                let hours: u32 = parts[0].trim().parse().ok()?;
                let minutes: u32 = parts[1].trim().parse().ok()?;
                let seconds: u32 = parts[2].trim().parse().ok()?;
                return Some(hours * 3600 + minutes * 60 + seconds);
            } else {
                // Assume format is mm:ss:ms, ignore milliseconds
                let minutes: u32 = parts[0].trim().parse().ok()?;
                let seconds: u32 = parts[1].trim().parse().ok()?;
                return Some(minutes * 60 + seconds);
            }
        }
        4 => {
            // Assume format is hh:mm:ss:ms
            let hours: u32 = parts[0].trim().parse().ok()?;
            let minutes: u32 = parts[1].trim().parse().ok()?;
            let seconds: u32 = parts[2].trim().parse().ok()?;
            return Some(hours * 3600 + minutes * 60 + seconds);
        }
        _ => return None,
    }
}
