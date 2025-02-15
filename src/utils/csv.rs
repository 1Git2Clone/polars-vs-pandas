use crate::prelude::*;
use rand::{
    distr::{Alphanumeric, SampleString},
    rng,
};
use std::{
    fs::OpenOptions,
    io::{BufWriter, Write},
    path::Path,
};

pub fn generate_csv_file<W: Write>(output: &mut W) -> io::Result<()> {
    let output_path = Path::new(env!("CARGO_MANIFEST_DIR")).join(CSV_PATH);

    if output_path.exists() {
        return Err(io::Error::new(
            io::ErrorKind::AlreadyExists,
            format!(
                "Path: `{}` already exists.",
                output_path.canonicalize()?.display()
            ),
        ));
    }

    let mut rng = rng();

    let file = OpenOptions::new()
        .create(true)
        .truncate(true)
        .write(true)
        .open(&output_path)
        .unwrap();
    let mut writer = BufWriter::new(file);

    writer.write_all(
        format!(
            "{}\n",
            (1..=COL_COUNT)
                .map(|i| format!("Header {}", i))
                .collect::<Vec<String>>()
                .join(",")
        )
        .as_bytes(),
    )?;

    for _ in 1..=ROW_COUNT {
        let row = format!(
            "{}\n",
            (1..=COL_COUNT)
                .map(|_| Alphanumeric.sample_string(&mut rng, COL_LEN))
                .collect::<Vec<String>>()
                .join(",")
        );

        writer.write_all(row.as_bytes())?;
    }
    writer.flush()?;

    writeln!(
        output,
        "File generated successfully in `{}`!",
        output_path.canonicalize()?.display()
    )?;

    Ok(())
}
