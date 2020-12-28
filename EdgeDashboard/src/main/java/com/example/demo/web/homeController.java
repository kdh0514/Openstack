package com.example.demo.web;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class homeController {
	
	//전역 변수로 받아온 값을 다른 곳에서 뿌려준다
	private String numPlateValue;
	
	//여기서 Get으로 받아온다
	@RequestMapping(value="/recorder", method = RequestMethod.GET)
	public String contentView(
			@RequestParam(name = "num") String num)
	{
		//전역 변수에 값 입력
		numPlateValue = num;
		System.out.println("Number Plate Text : " + num);

		return "Success!";
	}
	
	@Controller
	@RequestMapping("/")
	public class mainController {
		
		@GetMapping("")
		public String home() {
			System.out.println("?");
			return "home";
		}
		
	}
	
	@Controller
	@RequestMapping("/instance")
	public class instanceController {
		
		@GetMapping("")
		public String charts() {
			System.out.println("?");
			return "instance";
		}
		
	}
	
	@Controller
	@RequestMapping("/model")
	public class modelController {
		
		@GetMapping("")
		public String charts() {
			System.out.println("?");
			return "model";
		}
		
	}
	
	@Controller
	@RequestMapping("/collector")
	public class collectController {
		
		@GetMapping("")
		public String charts() {
			System.out.println("?");
			return "collector";
		}
		
	}
	
	@Controller
	@RequestMapping("/result")
	public class resultController {
		
		@GetMapping("")
		public String charts(Model model) {
			System.out.println("?");
			model.addAttribute("numText", numPlateValue);
			
			return "result";
		}
		
	}
	
}
