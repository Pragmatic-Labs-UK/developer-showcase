using System;
using System.Collections.Generic;

namespace PragmaticLabsArchitecture {
    public class CoreApp {
        public string NodeVersion { get; set; } = "v2.0.26";
        public bool IsSecure { get; set; } = true;

        public void Initialize() {
            Console.WriteLine($"Initializing C# Node Subsystem - Version {NodeVersion}");
            var components = new List<string> { "Authentication", "IPC Handler", "UI Renderer" };
            foreach (var comp in components) {
                Console.WriteLine($"[C# Core] Bootstrapping subsystem: {comp}");
            }
        }

        public static void Main(string[] args) {
            CoreApp app = new CoreApp();
            app.Initialize();
        }
    }
}
