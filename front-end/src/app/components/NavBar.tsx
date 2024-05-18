"use client";

import React from "react";
import {Navbar, NavbarBrand, NavbarContent, NavbarItem, Link, Button} from "@nextui-org/react";
import Profile from "./Profile";

export default function NavBar() {

  return (
    <Navbar>
      <NavbarBrand>
        <p className="font-bold text-inherit">AionNexus</p>
      </NavbarBrand>
      <NavbarContent className="hidden sm:flex gap-4" justify="center">
        <NavbarItem>
          <Link color="foreground" href="#">
            Features
          </Link>
        </NavbarItem>
        <NavbarItem isActive>
          <Link href="#" aria-current="page">
            Customers
          </Link>
        </NavbarItem>
        <NavbarItem>
          <Link color="foreground" href="#">
            Integrations
          </Link>
        </NavbarItem>
      </NavbarContent>
      <NavbarContent justify="end">
      <NavbarItem>
          <Profile></Profile>
        </NavbarItem>
        <NavbarItem>
          <Link color="primary" href="/api/auth/logout">
            Logout
          </Link>
        </NavbarItem>
      </NavbarContent>
    </Navbar>
  );
}
