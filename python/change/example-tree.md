min_coins(6)
├── use 1 → min_coins(5)
│ ├── use 1 → min_coins(4)
│ │ ├── use 1 → min_coins(3)
│ │ │ ├── use 1 → min_coins(2)
│ │ │ │ └── use 1 → min_coins(1)
│ │ │ │ └── use 1 → min_coins(0) ✓
│ │ │ └── use 3 → min_coins(0) ✓
│ │ ├── use 3 → min_coins(1)
│ │ │ └── use 1 → min_coins(0) ✓
│ │ └── use 4 → min_coins(0) ✓
│ ├── use 3 → min_coins(2)
│ │ └── use 1 → min_coins(1)
│ │ └── use 1 → min_coins(0) ✓
│ └── use 4 → min_coins(1)
│ └── use 1 → min_coins(0) ✓
├── use 3 → min_coins(3)
│ ├── use 1 → min_coins(2)
│ │ └── use 1 → min_coins(1)
│ │ └── use 1 → min_coins(0) ✓
│ └── use 3 → min_coins(0) ✓
└── use 4 → min_coins(2)
└── use 1 → min_coins(1)
└── use 1 → min_coins(0) ✓
