module Jekyll
  module JoinLinesFilter
    def join_lines(input)
      input.to_s.gsub(/\n */, "")
    end
  end
end

Liquid::Template.register_filter(Jekyll::JoinLinesFilter)
