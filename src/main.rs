/*!
Use this code to generate a 1 million random line 9 column (33 characters each) CSV file.

 NOTE: These settings are configurable.
*/

mod config;
mod prelude;
mod utils;

use prelude::*;

fn main() -> io::Result<()> {
    utils::generate_csv_file(&mut io::stdout().lock())?;

    Ok(())
}
