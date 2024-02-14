#include "Programm.h"
#include "imgui.h"
#include "misc/cpp/imgui_stdlib.h"
#include <cstdlib>
#include <sstream>
#include <cmath>
#include <iostream>

Programm* Programm::Instance = nullptr;

bool is_number(const std::string& s)
{
	return !s.empty() && std::find_if(s.begin(),
		s.end(), [](unsigned char c) { return !std::isdigit(c); }) == s.end();
}

Programm::Programm()
{
	//Buffer.resize(256);
	//Buffer = new char[BufSize];
}

Programm* Programm::GetProgramm()
{
	if (!Instance) {
		Instance = new Programm();
	}
	return Instance;
}

Programm::~Programm()
{
	//delete[] Buffer;
}

void Programm::DoActions()
{
	ImGui::SetNextWindowPos(ImGui::GetMainViewport()->Pos);
	ImGui::SetNextWindowSize(ImGui::GetMainViewport()->Size);
	ImGui::Begin("My window", &close /*, ImGuiWindowFlags_... */);
	{
		
		if (!close) {
			ImGui::Begin("Close");
			ImGui::Text("Do you really want to close application?");
			if (ImGui::Button("No")) {
				close = true;
			}
			ImGui::SameLine();
			if (ImGui::Button("Yes")) {
				*CloseImpl = true;
			}
			ImGui::End();
		}


		//ImGui::InputFloat("Input field");
		//ImGui::InputText("Input field", &Buffer);
		float* fptr = &AArg;
		std::stringstream stream;
		//if (Buffer.size()) {
		//	if (is_number(Buffer)) {
				if (DivPressed) {
					fptr = &BArg;
					//ImGui::InputFloat("Input field", &BArg);
					//delete BArg;
					//BArg = new float(std::stof(Buffer));
				}
				else {
					fptr = &AArg;
					//ImGui::InputFloat("Input field", &AArg);
					//delete AArg;
					//AArg = new float(std::stof(Buffer));
				}
		//		Buffer.clear();
		//	}
		//}
		ImGui::InputFloat("Input field", fptr);
		if (ResultPressed && AArg && ArccosPressed) {
			stream << acos(AArg);
			ResultPressed = false;
			stream >> OutBuffer;
			ArccosPressed = false;
		}
		if (ResultPressed  && AArg && BArg && DivPressed) {
			if (BArg == 0) {
				stream << "invalid";
			}
			else {
				stream << AArg / BArg;
			}
			ResultPressed = false;
			stream >> OutBuffer;
			DivPressed = false;
		}

		//std::cout << AArg << " " << BArg << std::endl;
		ImGui::TextWrapped(OutBuffer.c_str());
		//ImGui::BeginTable("", 3);
		

		ImGui::BeginTable("", 3);
		ImGui::TableNextColumn(); if (ImGui::Button("arccos")) { ArccosPressed = true; }
		ImGui::TableNextColumn(); ImGui::Spacing();
		ImGui::TableNextColumn(); if (ImGui::Button("clear")) { Buffer.clear(); OutBuffer.clear(); AArg = 0; BArg = 0; }
		ImGui::TableNextColumn(); ImGui::Spacing();
		ImGui::TableNextColumn(); if (ImGui::Button("/")) {	DivPressed = true;}
		ImGui::TableNextColumn(); ImGui::Spacing();
		ImGui::TableNextColumn(); ImGui::Spacing();
		ImGui::TableNextColumn(); ImGui::Spacing();
		ImGui::TableNextColumn(); if (ImGui::Button("Result")) { ResultPressed = true;}
		ImGui::EndTable();
	}

	ImGui::End();
}
