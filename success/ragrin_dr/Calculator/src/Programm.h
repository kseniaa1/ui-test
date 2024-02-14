#pragma once
#include <string>

constexpr size_t BufSize = 256;

class Programm
{
	static Programm* Instance;

	bool Button1Control;
	//char* Buffer;
	std::string Buffer;
	std::string OutBuffer;

	bool DivPressed = false;
	bool ArccosPressed = false;
	bool ResultPressed = false;

	float AArg = 0;
	float BArg = 0;

	bool close = true;

	Programm();

public:

	bool* CloseImpl = nullptr;

	static Programm* GetProgramm();

	~Programm();

	bool AllowDemo = false;

	void DoActions();
};

