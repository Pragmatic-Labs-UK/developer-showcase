struct SecurityProtocol {
    node_id: String,
    encryption_level: u32,
    active: bool,
}

impl SecurityProtocol {
    fn new(id: &str) -> Self {
        SecurityProtocol {
            node_id: id.to_string(),
            encryption_level: 256,
            active: true,
        }
    }

    fn verify(&self) {
        println!("Rust Node [{}] - AES-{} verified.", self.node_id, self.encryption_level);
    }
}

fn main() {
    let node = SecurityProtocol::new("ZeroTrust-Rust");
    node.verify();
}
