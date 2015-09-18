#!/usr/local/bin/perl

use strict;
use warnings;
use Lucy::Simple;

#
# Ensure the index directory is both available and empty.
#
my $index = "/ppant/LucyTest/index";
system( "rm", "-rf", $index );
system( "mkdir", "-p", $index );


#  Create the helper...a new Lucy::Simple object 
my $lucy = Lucy::Simple->new( path => $index, language => 'en', );

# Add the first "document". (We are mainly adding meta data of the document)
my %one = ( title => "This is a title of first article" , body => "some text inside the body we need to test the implementaion of lucy", id => 1 );
$lucy->add_doc( \%one );

# Add the second "document".
my %two = ( title => "This is another article" , body => "I am putting some basic content, using some words which are also in first document like implementation", id => 2 );
$lucy->add_doc( \%two );
# Both the documents are now indexed in path