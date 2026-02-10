#!/bin/bash

# System Monitor Pro - Setup Script
# Makes installation and running easy

set -e  # Exit on error

echo ""
echo "╔══════════════════════════════════════════╗"
echo "║     System Monitor Pro - Setup          ║"
echo "╚══════════════════════════════════════════╝"
echo ""

# Colors for better output
GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check Python
echo -e "${BLUE}[1/4] Checking Python...${NC}"
if command -v python3 &> /dev/null; then
    python_version=$(python3 --version | cut -d' ' -f2)
    echo -e "  ${GREEN}✓ Python $python_version found${NC}"
else
    echo -e "  ${RED}✗ Python3 is not installed${NC}"
    echo -e "\nPlease install Python3 from: https://python.org"
    exit 1
fi

# Install psutil
echo -e "\n${BLUE}[2/4] Installing dependencies...${NC}"
if python3 -c "import psutil" &> /dev/null; then
    psutil_version=$(python3 -c "import psutil; print(psutil.__version__)")
    echo -e "  ${GREEN}✓ psutil $psutil_version already installed${NC}"
else
    echo -e "  Installing psutil library..."
    pip3 install psutil --quiet
    echo -e "  ${GREEN}✓ psutil installed successfully${NC}"
fi

# Make script executable
echo -e "\n${BLUE}[3/4] Setting up permissions...${NC}"
chmod +x setup.sh
echo -e "  ${GREEN}✓ Setup script is now executable${NC}"

# Create logs directory
echo -e "\n${BLUE}[4/4] Creating directory structure...${NC}"
mkdir -p logs
echo -e "  ${GREEN}✓ Created logs/ directory${NC}"

# Success message
echo -e "\n${GREEN}══════════════════════════════════════════${NC}"
echo -e "${GREEN}✅ Setup completed successfully!${NC}"
echo -e "${GREEN}══════════════════════════════════════════${NC}"

echo -e "\n${BLUE}How to run:${NC}"
echo -e "  ${GREEN}python monitor.py${NC}               # Interactive menu"
echo -e "  ${GREEN}python monitor.py once${NC}          # Run once"
echo -e "  ${GREEN}python monitor.py start${NC}         # Continuous monitoring"
echo -e "  ${GREEN}python monitor.py summary${NC}       # View logged data"
echo -e "  ${GREEN}python monitor.py help${NC}          # Show help"

echo -e "\n${BLUE}Quick test:${NC}"
echo -e "  ${GREEN}python monitor.py once${NC}"
echo ""